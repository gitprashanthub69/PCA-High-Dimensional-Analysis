// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract DigitalNotebook {

    // Struct to store a single note
    struct Note {
        string message;
        uint timestamp;
    }

    // Mapping from user address to their notes
    mapping(address => Note[]) private userNotes;

    // Bonus: global counter to track total notes created by all users
    uint public totalNotes;

    // Function to add a new note
    function addNote(string memory _message) public {
        userNotes[msg.sender].push(
            Note({
                message: _message,
                timestamp: block.timestamp
            })
        );

        // Increment global counter
        totalNotes++;
    }

    // Function to retrieve all notes of the caller
    function getNotes() public view returns (Note[] memory) {
        return userNotes[msg.sender];
    }
}
