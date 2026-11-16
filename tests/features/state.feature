Feature: state.json, the repositories the release control plane acts on
  pubfleet reads state.json for the board, the nightly and the rulesets.
  These scenarios read it as pubfleet does, offline; `state / valid` also
  asks GitHub that each repository exists and holds what its roles need.

  Scenario: state.json has the shape pubfleet reads
    Given the state file
    Then pubfleet finds nothing wrong with its shape

  Scenario: Every repository it names is under its owner, once
    Given the state file
    Then each repository is named once, under the state's owner

  Scenario Outline: The repos file for the <role> lists exactly the repositories with <role> on
    Given the state file
    When pubfleet writes the repos file for the <role>
    Then it lists each repository with <role> on, and no other

    Examples:
      | role   |
      | board  |
      | govern |
