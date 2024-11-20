##################################################################
Stakeholder Specification Evaluation for Merge Python Dictionaries
##################################################################

.. evaluation:: Missing name of the tool / script
   :id: EVAL_STAKE_MISSING_NAME
   :evaluated: CSTRQ_MERGE_DICTS, CSTRQ_DETECT_MERGE_CONFLICTS
   :output: SWRQ_TOOL_merge_dicts

   As the stakeholders did not defined the name of the tool / script
   we have to define it. See output requirement.



.. evaluation:: Explicit definition of "dictionaries"
   :id: EVAL_STAKE_MANY_DICTS
   :evaluated: CSTRQ_MERGE_DICTS
   :output: SWRQ_MERGE_DICTS, SWRQ_LIST_OF_DICTS

   The :need:`CSTRQ_MERGE_DICTS` does define to "merge dictionaries".
   So we made it avaialbe it as software requirement, in :need:`SWRQ_MERGE_DICTS`.
   We want to make it more obvious that this means even `none`, `one`, `two` and `more` dictionaries.
   Even we improve the description in the :need:`SWRQ_LIST_OF_DICTS` to explicit mention a
   list of dictionaries.



.. evaluation:: Merge python dictionaries
   :id: EVAL_STAKE_DOUBLE_DEFINITON_ALLOWED
   :evaluated: CSTRQ_DETECT_MERGE_CONFLICTS
   :output: SWRQ_ALLOW_DOUBLE_DEFINITION

   The :need:`CSTRQ_MERGE_DICTS` does define a merge conflict as
   same Key and different Value.
   So we derive that the same key and same Value is not a merge conflict.



.. evaluation:: Invalid input
   :id: EVAL_STAKE_MISSING_INVALID_INPUT
   :evaluated: CSTRQ_MERGE_DICTS, CSTRQ_DETECT_MERGE_CONFLICTS
   :output: SWRQ_LIST_OF_DICTS

   The stakeholder requirements are not defining the behavior in
   case not valid input is provided.

   So we define if we get something else than a list or empty list,
   we ill indicate the appropriate python exception for invalid
   type: `AttributeError`



.. evaluation:: Missing definition for output in case of merge conflict
   :id: EVAL_STAKE_OUTPUT_CONFLICT
   :evaluated: CSTRQ_MERGE_DICTS, CSTRQ_DETECT_MERGE_CONFLICTS
   :output: SWRQ_USE_FIRST_VALUE_FOR_KEY

   In some cases, a merge conflict is not stop sign.
   It is possible to proceed, if we define the merge behavior in such case:

   If we have the same key in two dictionaries but different content,
   the first value shall be in the final dict.

