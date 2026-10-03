/**
 * @name Tainted data passed to validate() reaches a code injection sink
 * @description Arguments to validate() are treated as untrusted.
 * @kind path-problem
 * @problem.severity error
 * @precision medium
 * @id py/per-validate-taint
 * @tags security
 */

import python
import semmle.python.dataflow.new.DataFlow
import semmle.python.dataflow.new.RemoteFlowSources
import semmle.python.ApiGraphs
import semmle.python.security.dataflow.CodeInjectionQuery
import CodeInjectionFlow::PathGraph

class PerValidateSource extends RemoteFlowSource::Range {
  PerValidateSource() {
    // inside the library: parameters of validate()
    this.(DataFlow::ParameterNode).getParameter() =
      any(Function f | f.getName() = "validate").getAnArg()
    or
    // in other repos: arguments at calls to validate()
    this = API::moduleImport("enforce_rules").getMember("validate").getACall().getArg(_)
  }

  override string getSourceType() { result = "argument to validate()" }
}

from CodeInjectionFlow::PathNode source, CodeInjectionFlow::PathNode sink
where CodeInjectionFlow::flowPath(source, sink)
select sink.getNode(), source, sink,
  "Data from $@ reaches a code injection sink.",
  source.getNode(), "a validate() argument"
