import python
import semmle.python.dataflow.TaintTracking

/**
 * All arguments to validate(...) are taint sources.
 */
class ValidateArgSource extends TaintTracking::SourceNode {
  ValidateArgSource() {
    exists(FunctionCall fc |
      fc.getCallee().getName() = "validate" and
      this = fc.getArgument(_)
    )
  }
}

/**
 * All arguments to is_valid(...) are taint sources.
 */
class IsValidArgSource extends TaintTracking::SourceNode {
  IsValidArgSource() {
    exists(FunctionCall fc |
      fc.getCallee().getName() = "is_valid" and
      this = fc.getArgument(_)
    )
  }
}
