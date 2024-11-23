############################
Tests report for merge_dicts
############################

The following table shows the test specifications:

.. needtable::
   :columns: id, title
   :types: test_spec
   :style: datatables

The following table shows the software requirements not successful passed the tests:

.. needtable::
   :filter: type == 'sw_req' and test_status == 'verified_passed'
   :columns: id, title
   :style: datatables

.. needpie:: Software requirements with test status
   :labels: Passed, Failed
   :legend:
   :colors: green, red

   type == 'sw_req' and test_status == 'verified_passed'
   type == 'sw_req' and test_status != 'verified_passed'

Here are metrics for all engineering artifacts needed.
Contribution via pull requests is requested.
