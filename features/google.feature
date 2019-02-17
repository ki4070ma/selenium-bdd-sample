Feature: Google search page

  Scenario: Visit google and check
     When we visit google
     Then it should have a title "Google"

  Scenario: input word at search page
     When we input "hogehoge" to text box at search page
     Then it should have "hogehoge" at text box
