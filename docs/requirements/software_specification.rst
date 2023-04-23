###########################################
Specification for Merge Python Dictionaries
###########################################

.. sw_req:: Name of the tool: merge_dicts
   :id: SWRQ_TOOL_merge_dicts
   :status: verified

   The tool / script shall be defined as `merge_dicts`.



.. sw_req:: Merge python dictionaries
   :id: SWRQ_MERGE_DICTS
   :status: verified
   :satisfies: CSTRQ_MERGE_DICTS

   The python module `merge_dicts` shall provide a function to merge a list of
   python dictionaries to one dictionary.



.. sw_req:: Definition: list of dictionaries
   :id: SWRQ_LIST_OF_DICTS
   :status: verified
   :satisfies: CSTRQ_MERGE_DICTS

   The above defined function to merge dictionaries shall treat list as:
   non, one, two or many dictionaries organized in a list.

   .. verify:: Test function with appropriate number of dictionaries
      :id: VERIFY_SWRQ_LIST_OF_DICTS

      Test function with:
      
      - empty list
      - one dictionary in the list
      - two dictionary in the list
      - three dictionary in the list (many)

      With python it is difficult to test the upper bound.



.. sw_req:: Detect merge conflicts
   :id: SWRQ_DETECT_MERGE_CONFLICTS
   :status: verified
   :satisfies: CSTRQ_DETECT_MERGE_CONFLICTS

   As multiple dictionaries could have for the same Key different
   defined Values, `merge_dicts` shall report merge conflicts.

   .. verify:: test merge conflict is indicated.
      :id: VERIFY_SWRQ_DETECT_MERGE_CONFLICTS

      Verify that `merge_dicts` reports a merge conflict if
      different values but same key in dictionaries are provided.



.. sw_req:: Allow double definitions of same Key / Value
   :id: SWRQ_ALLOW_DOUBLE_DEFINITION
   :status: verified
   :satisfies: CSTRQ_DETECT_MERGE_CONFLICTS

   The definition of the same Key/Value Pair is allowed and
   shall **not** reported as a merge conflict.

   .. verify:: Allow double definition
      :id: VERIFY_SWRQ_ALLOW_DOUBLE_DEFINITION

      Verify with a test case, that a double definition of a Key / Value pair lead **not**
      to a merge conflict indication.



.. sw_req:: Output in merge conflict case
   :id: SWRQ_USE_FIRST_VALUE_FOR_KEY
   :status: verified
   :satisfies: CSTRQ_DETECT_MERGE_CONFLICTS

   If we have the same key in two dictionaries but different content,
   the first defined value shall be in the final dictionary.

   .. verify:: Output in merge conflict case
      :id: VERIFY_SWRQ_USE_FIRST_VALUE_FOR_KEY

      Verify with a test case:

      1. Use merge function with double defined Key/Value
      2. Test that values from the first element in the list are in the output.

