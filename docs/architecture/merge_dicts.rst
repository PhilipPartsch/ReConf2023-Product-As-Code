#########################
Architecture: merge_dicts
#########################

.. package:: merge_dicts
    :id: P_MERGE_DICTS
    :satisfies: [[fetch_elements(filter = "type == 'sw_req'")]]


.. arch_module:: merge_dicts
   :id: M_MERGE_DICTS
   :satisfies: SWRQ_TOOL_merge_dicts, SWRQ_MERGE_DICTS
   :implements: IF_MERGE_DICTS

   **Element**

   .. needarch::

      rectangle "{{need().title}}" as {{need().id}} {{ref(need().id)}}

   .. instead of explicit manual definition of needarch, we could even use {{flow(need().id)}}
      to achieve the same.


   **Architecture with interfaces**

   .. needarch::
      :key: class
      :debug:

      {{uml(need().id)}}
      {{import("implements")}}
      {% for e in need().implements %}
      {{e}} - {{need().id}}
      {% endfor %}


   Implementation:

   .. autosummary::

      merge_dicts


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



.. interface:: merge_dicts
   :id: IF_MERGE_DICTS
   :satisfies: SWRQ_MERGE_DICTS, SWRQ_DETECT_MERGE_CONFLICTS, SWRQ_ALLOW_DOUBLE_DEFINITION, SWRQ_USE_FIRST_VALUE_FOR_KEY
   :verified_by: TCOVER_MERGE_DICTS

   **Architecture**

   .. needarch::

      interface "{{need().title}}" as {{need().id}} {{ref(need().id, text = "")}}

   .. instead of explicit manual definition of needarch, we could even use `{{flow(need().id)}}`
      to achieve the same.

   Implementation: :py:func:`merge_dicts.merge_dicts`

   .. decision:: Complexity of interface
      :id: D_IF_MERGE_DICTS

      The requirements can be implemented in this interface,
      so we do not need a complex implementation in the module.




