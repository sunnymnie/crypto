pragma solidity >=0.6.0 < 0.9.0;
// Can do pragma solidity ^0.6.0 for 0.6.x

//TODO: Start at 2:00:00

// Define contract (class)
contract SimpleStorage{

    uint256 favoriteNumber; //Inits to zero, is public-->technically a view function

    struct Person {
        uint256 favoriteNumber;
        string name;
    }

    Person public person = Person({favoriteNumber:2, name:"Emily"});

    Person[] public people;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    //view, pure are read-only thus not need to make transaction
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    //pure only does math does not interact with the blockchain
    function calc(uint256 num) public pure returns (uint256 answer) {
        return num + num;
    }

    // string is array of bytes, can choose to store in memory or storage (persist after function call)
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(Person({_favoriteNumber, _name}));
    }

}
