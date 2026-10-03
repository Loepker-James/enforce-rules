/**
 * @name Tainted data passed to validate() reaches a sink
 * @description Every parameter of validate() is treated as untrusted.
 *              Reports where that data reaches a dangerous operation.
 * @kind path-problem
 * @problem.severity error
 * @precision medium
 * @id py/per-validate-taint
 * @tags security
 */

import python
import semmle.python.dataflow.new.DataFlow
import semmle.python.dataflow.new.TaintTracking
import semmle.python.ApiGraphs

module ValidateConfig implements DataFlow::ConfigSig {
  predicate isSource(DataFlow::Node n) {
    exists(Function f |
      f.getName() = "validate" and
      n.(DataFlow::ParameterNode).getParameter() = f.getAnArg()
    )
  }

  predicate isSink(DataFlow::Node n) {
    n = API::builtin("eval").getACall().getArg(0)
    or
    n = API::builtin("exec").getACall().getArg(0)
  }
}

module ValidateFlow = TaintTracking::Global<ValidateConfig>;
import ValidateFlow::PathGraph

from ValidateFlow::PathNode source, ValidateFlow::PathNode sink
where ValidateFlow::flowPath(source, sink)
select sink.getNode(), source, sink,
  "Data from validate() parameter $@ reaches this sink.",
  source.getNode(), source.getNode().toString()
