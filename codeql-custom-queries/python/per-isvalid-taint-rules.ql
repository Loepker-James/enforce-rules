/**
 * @name Tainted data passed to is_valid() reaches a code injection sink
 * @description Arguments to is_valid() are treated as untrusted.
 * @kind path-problem
 * @problem.severity error
 * @precision medium
 * @id py/per-is_valid-taint
 * @tags security
 */

import python
import semmle.python.dataflow.new.DataFlow
import semmle.python.dataflow.new.RemoteFlowSources
import semmle.python.ApiGraphs
import semmle.python.security.dataflow.CodeInjectionQuery
import CodeInjectionFlow::PathGraph

class Peris_validSource extends RemoteFlowSource::Range {
  Peris_validSource() {
    // inside the library: parameters of is_valid()
    this.(DataFlow::ParameterNode).getParameter() =
      any(Function f | f.getName() = "is_valid").getAnArg()
    or
    // in other repos: arguments at calls to is_valid()
    this = API::moduleImport("enforce_rules").getMember("is_valid").getACall().getArg(_)
  }

  override string getSourceType() { result = "argument to is_valid()" }
}

from CodeInjectionFlow::PathNode source, CodeInjectionFlow::PathNode sink
where CodeInjectionFlow::flowPath(source, sink)
select sink.getNode(), source, sink,
  "Data from $@ reaches a code injection sink.",
  source.getNode(), "a is_valid() argument"
