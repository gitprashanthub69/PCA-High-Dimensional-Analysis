// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FraudStorage {

    struct Record {
        string hashValue;
        bool isFraud;
        uint256 timestamp;
    }

    mapping(string => Record) private records;

    event RecordAdded(string hashValue, bool isFraud, uint256 timestamp);

    function addRecord(string memory _hash, bool _isFraud) public {
        records[_hash] = Record(_hash, _isFraud, block.timestamp);
        emit RecordAdded(_hash, _isFraud, block.timestamp);
    }

    function getRecord(string memory _hash)
        public
        view
        returns (bool, uint256)
    {
        Record memory r = records[_hash];
        return (r.isFraud, r.timestamp);
    }
}
