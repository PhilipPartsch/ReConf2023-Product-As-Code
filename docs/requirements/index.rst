#####################################
Requirement Specifications & Overview
#####################################


**************
Specifications
**************

.. toctree::
   :maxdepth: 1
   
   stakeholder_specification
   stakeholder_specification_evaluation
   software_specification



********
Overview
********

**Ratio of requirement types**

.. needpie:: Ratio of requirement types
   :labels: Stakeholder Requirement, Software Requirement, Evaluation

   type == 'stake_req'
   type == 'sw_req'
   type == 'evaluation'


**Requiremennts & Status Overview**

.. needbar:: Requirements & Status Overview
   :legend:
   :colors: black, yellow, orange, green
   :xlabels: FROM_DATA
   :ylabels: FROM_DATA

              ,        Stakeholder Requirement             ,           Software Requirement
         empty, type=='stake_req' and status==''           ,    type=='sw_req' and status==''
      accepted, type=='stake_req' and status=='accepted'   ,    type=='sw_req' and status=='accepted'
   implemented, type=='stake_req' and status=='implemented',    type=='sw_req' and status=='implemented'
      verified, type=='stake_req' and status=='verified'   ,    type=='sw_req' and status=='verified'


**Requirement Linkage**

.. needflow:: Requirement Linkage
   :types: stake_req, sw_req
   :show_link_names:
   :show_filters:


**V-Model**

.. needflow:: V-Model
   :types: stake_req, sw_req, arch_module, if, test_spec, testfile, test_coverage
   :show_link_names:
   :show_filters:


**Example for reporting / Tables**

.. needtable:: List of software requirements
   :types: sw_req
   :style: table
   :columns: id;title;docname as "document";lineno as "line no"
   :sort: lineno
