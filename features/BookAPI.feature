Feature: Verify if Books are added and deleted using Library API

    Scenario: Verify Addbook API functionality
        Given the Book details which need to be added to Library
        When we execute the AddBook PostPI method
        Then book is successfully added