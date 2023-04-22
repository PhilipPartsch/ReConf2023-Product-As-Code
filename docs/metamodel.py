

# global
main_color = "#164293"
link_color = "#89037A"



# sphinx_needs configuration
needs_id_regex = '^[A-Za-z0-9_-]{3,}'

# Define project specific needs directives

needs_types = [
               # Process-As-Code
               # Role
               dict(directive="prole", title="Role", prefix="ROLE_", color="#ffffff", style="actor"),

               # Strategy
               dict(directive="strategy", title="Strategy", prefix="STGY_", color="#ffffff", style="hexagon"),

               # Process
               dict(directive="process", title="Process", prefix="PROC_", color="#ffffff", style="package"),
               dict(directive="activity", title="Activity", prefix="ACT_", color="#ffffff", style="card"),
               dict(directive="artifact", title="Artifact", prefix="ART_", color="#ffffff", style="artifact"),
               dict(directive="pstatus", title="Status", prefix="STATUS_", color="#ffffff", style="artifact"), # Child of Artifact

               # Instruction
               dict(directive="template", title="Template", prefix="TEMP_", color="#ffffff", style="frame"),
               dict(directive="instruction", title="Work Instruction", prefix="INST_", color="#ffffff", style="frame"),

               # Storage
               dict(directive="repo", title="Repository", prefix="REPO_", color="#ffffff", style="database"),

               # Timeline
               dict(directive="lifecycle", title="Lifecycle", prefix="CYCLE_", color="#ffffff", style="card"),
               dict(directive="phase", title="Phase", prefix="PHASE_", color="#ffffff", style="rectangle"),
               dict(directive="milestone", title="Milestone", prefix="MILE_", color="#ffffff", style="hexagon"),

               # Product-As-Code

               # Requirements
               dict(directive="stake_req", title="Stakeholder Requirement", prefix="CSTRQ_", color="#abcdef", style="artifact"),
               dict(directive="sys_req", title="System Requirement", prefix="SYSRQ_", color="#abcdef", style="artifact"),
               dict(directive="sw_req", title="Software Requirement", prefix="SWRQ_", color="#abcdef", style="artifact"),

               # Architecture & Design
               dict(directive="bin", title="Binary", prefix="BIN_", color="#abcdef", style="rectangle"),
               dict(directive="lib", title="Library ", prefix="LIB_", color="#abcdef", style="rectangle"),
               dict(directive="package", title="Package", prefix="P_", color="#abcdef", style="package"),
               dict(directive="arch_module", title="Module", prefix="M_", color="#abcdef", style="package"),
               dict(directive="comp", title="Component", prefix="C_", color="#abcdef", style="component"),
               dict(directive="unit", title="Unit", prefix="U_", color="#abcdef", style="rectangle"),
               dict(directive="if", title="Interface", prefix="IF_", color="#abcdef", style="interface"),
               dict(directive="decision", title="Decision", prefix="D_", color="#efff9c", style="artifact"),

               # Test
               dict(directive="test_spec", title="Test Specification", prefix="TS_", color="#abcdef", style="artifact"),
               dict(directive="test_coverage", title="Test Coverage", prefix="TCOVER_", color="#abcdef", style="artifact"),
               dict(directive="sys_test", title="System Test", prefix="SYSTST_", color="#abcdef", style="artifact"),
               dict(directive="sw_test", title="Software Test", prefix="SWTST_", color="#abcdef", style="artifact"),

               # Generic
               dict(directive="evaluation", title="Evaluation", prefix="EVAL_", color="#abcdef", style="artifact"),
               dict(directive="verify", title="Verification Information", prefix="VERIFY_", color="#abcdef", style="artifact"),

              ]

# Define extra options for needs object
needs_extra_options = [
   'author', # to store the author of a stakeholder requirement
   'safety_level',
   'security_level',
   'reject_reason',
   'coverage', # to store test coverage in %
   'pathfile', # file path in needs e.g. for test coverage
   'interface_definition', # to store in machine readable code interface definition
]

needs_services = {}

needs_extra_links = [
   #Used to indicate a generic description is been specialized
   {
      "option": "derived",
      "incoming": "Detailed in",
      "outgoing": "Derived from",
      "style": "#000000",
      "style_start": "-",
      "style_end": "-<>",
   },
   # Process to Process link
   {
      "option": "successor",
      "incoming": "Predecessor",
      "outgoing": "Successor",
      "style": "#000000",
      "style_start": "-",
      "style_end": "right->",
   },
   # Process to Activity link
   {
      "option": "activities",
      "incoming": "Process",
      "outgoing": "Activities",
      "style": "#000000",
   },
   # Activity to Phase link
   {
      "option": "when",
      "incoming": "contains",
      "outgoing": "executed in",
   },
   # Activity to Work Instruction link
   {
      "option": "instruction",
      "incoming": "Activity",
      "outgoing": "Instruction",
      "style": "#000000",
   },
   # links from Activity to Artifacts
   {
      "option": "input",
      "incoming": "consumed by",
      "outgoing": "input",
      "style": "#000000",
      "style_start": "<-",
      "style_end": "-",
   },
   {
      "option": "output",
      "incoming": "generated by",
      "outgoing": "output",
      "style": "#000000",
   },
   # links to roles
   {# responsible:
      "option": "responsible",
      "incoming": "Responsible for",
      "outgoing": "Responsible",
      "style": "#000000",
      "style_start": ".",
      "style_end": "up.",
   },
   { # part of - to indicate that this role is a part of another role
      "option": "part_of",
      "incoming": "Includes",
      "outgoing": "Part of",
      "style": "#000000",
   },
   # links to repos and artifacts (an artifact can be stored in another artifact)
   {
      "option": "stored_in",
      "incoming": "to be stored",
      "outgoing": "stored in",
      "style": "#000000",
   },
   # link to a artifact from a template
   {
      "option": "blue_print",
      "incoming": "Template",
      "outgoing": "Template for",
      "style": "#000000",
   },
   # link to a process justification
   {
      "option": "why",
      "incoming": "Resolved with",
      "outgoing": "Justification",
      "style": "#000000",
   },
   # link from a software requirement to stakeholder requirement
   {
      "option": "satisfies",
      "incoming": "is satisfied by",
      "outgoing": "satisfies",
      "style_start": "-up",
      "style_end": "->",
   },
   # link from a requirement or archiecture element to a test specifiction
      {
      "option": "tests",
      "incoming": "tested by",
      "outgoing": "tests",
      "style_start": "-up",
      "style_end": "->"
   },
   {
      "option": "verfied_by",
      "incoming": "verfies",
      "outgoing": "verfied by",
      "style_start": "<-up",
      "style_end": "-"
   },
   # link from a requirement to an archiecture element
   {
      "option": "implemented_by",
      "incoming": "implemented by",
      "outgoing": "implements"
   },
   # from evaluation report to artifact under evalaution
   {
      "option": "evaluated",
      "incoming": "evaluated by",
      "outgoing": "evaluated",
      "style_start": "-up",
      "style_end": "->",
   },
   
   {
      "option": "implements",
      "incoming": "implemented by",
      "outgoing": "implements",
      "style_start": "-up",
      "style_end": "->"
   },

]

needs_layouts = {
    'stakeholder_requirement': {
        'grid': 'simple_side_right_partial',
        'layout': {
            'head': [
                '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>>  <<collapse_button("meta", '
                'collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=False)>> '
            ],
            'meta': ['<<meta_all(no_links=True, exclude=["layout",])>>', '<<meta_links_all()>>'],
            'side': ['<<image("https://avatars.githubusercontent.com/{{author}}", align="center", is_external=True)>>',],
        }
    },
}


needs_functions = []

needs_global_options = {
    'layout': [ 
        #('stakeholder_requirement', 'type=="stake_req"'),
    ],
}

needs_render_context = {
}

needs_warnings = {
    'artifact_without_stored_in_link': "type == 'artifact' and len(stored_in) == 0",
    'stakeholder_requirement_without_author': "type == 'stake_req' and not author",
    #'author_only_allowed_for_stakeholder_requirement': "type != 'stake_req' and author",
    'evaluation_output_and_evaluated_needed': "type == 'evaluation' and (len(output) == 0 or len(evaluated) == 0)",
    'invalid_status' : "status and status not in ['accepted', 'implemented', 'verified']",
}


# _not_following_naming_convention
for type in needs_types:

    warn_text = type['directive'] + '_not_following_naming_convention'
    if warn_text not in needs_warnings:
        warn_test = "type == '" + type['directive'] + "' and not id.startswith('" + type['prefix'] + "')"
        needs_warnings[warn_text] = warn_test
    else:
        # todo: add warning
        pass

needs_string_links = {
    # Links to the related github user
    'github_user': {
        'regex': r'^(?P<value>\w+)$',
        'link_url': 'https://github.com/{{value}}',
        'link_name': 'GitHub User {{value}}',
        'options': ['author'],
    },
}
