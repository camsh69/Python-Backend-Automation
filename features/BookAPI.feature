Feature: Verify if Books are added and deleted using Library API

    @library
    Scenario: Verify Addbook API functionality
        Given the Book details which need to be added to Library
        When we execute the AddBook PostPI method
        Then book is successfully added

    @library
    Scenario Outline: Verify Addbook API functionality
        Given the Book details with <isbn> and <aisle>
        When we execute the AddBook PostPI method
        Then book is successfully added

        Examples:
            | isbn  | aisle |
            | hdsgh | 654   |
            | srdat | 837   |