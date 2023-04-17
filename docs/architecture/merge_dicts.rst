#########################
Architecture: merge_dicts
#########################


.. arch_module:: merge_dicts
   :id: M_MERGE_DICTS
   :satisfies: SWRQ_TOOL_merge_dicts, CSTRQ_MERGE_DICTS
   :implements: IF_MERGE_DICTS

   **Architecture**

   .. needarch::

      package merge_dicts

   **Architecture generated from datamodel**

   .. needflow:: Links
      :filter-func: filter.filter_id_linked_element_and_back(M_MERGE_DICTS, implements)
      :link_types: implements
      :show_link_names:
      :align: left

   .. decision:: Complexity of module
      :id: D_M_MERGE_DICTS

      The requirements can be implemented in one function,
      so we do not need a complex implementation in the module.



.. if:: merge_dicts
   :id: IF_MERGE_DICTS
   :satisfies: CSTRQ_MERGE_DICTS, SWRQ_DETECT_MERGE_CONFLICTS, SWRQ_ALLOW_DOUBLE_DEFINITION, SWRQ_USE_FIRST_VALUE_FOR_KEY
   :verfied_by: TCOVER_MERGE_DICTS

   **Architecture**

   .. needarch::

      interface merge_dicts

   .. decision:: Complexity of interface
      :id: D_IF_MERGE_DICTS

      The requirements can be implemented in this interface,
      so we do not need a complex implementation in the module.




