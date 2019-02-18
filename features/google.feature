Feature: Google search page

  Scenario: input word at search page
     When we input "hogehoge" to text box at search page
     Then it should have "hogehoge" at text box

  @test
  Scenario: search "Google Testing Blog" by google
     When we search with "Google Testing Blog" as query at search page
     Then Result page should have "Google Testing Blog" at the top of results
