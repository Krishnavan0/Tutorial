// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.2.0 <0.9.0;

contract MyContract {
    function helloWorld() public pure returns (string memory) {
        return "Hello, World!";
    }
}

contract identity{
   string name;
   uint age;

   constructor() {
      name = "Solidity";
      age = 25;
   }
   function getName() view public returns(string memory){
      return name;
   }
   function getAge() view public returns(uint){
      return age;
   }
   function setAge() public {
      age = age+2;
   }
}

contract state{
    uint public age;
    function setAge() public{
        age = 10;
    }
}

contract local{
    function store() pure public returns(uint){
        uint age = 10;
        return age;
    }
}

// Setter and Getter Method
contract GetSet{
   uint age = 10;
   function getter () public view returns(uint){
      return age;
   }
   function setter () public{
      age = age + 1;
   }
   function setter (uint newage) public{
      age = newage;
   }
}

// Constructor
contract construct{
   uint public count;
   constructor(uint newCount){
      count = newCount;
   }
}

// Integer
contract integer{
   uint8 public money = 255;
   function setter() public{
      money = money + 1;
   }
}

// Array
contract array{
   uint [6] public arr = [10,20,30,40,50,60];
   function setter(uint index, uint value) public{
      arr[index] = value;
   }
   function length() public view returns(uint){
      return arr.length;
   }
}

// Dynamic Array
contract dynamicArray{
   uint [] public arr;
   function pushElement(uint item) public{
      arr.push(item);
   }
   function len() public view returns(uint){
      return arr.length;
   }
   function popElement() public{
      arr.pop();
   }
}

// Bytes
contract Bytes{
   bytes3 public b3;
   bytes4 public b4;
   function setter() public{
      b3 = 'a%L';
      b4 = 'Z$3@';
   }
}

// Dynamic Bytes
contract dynamicBytes{
    bytes public b1='abc';
    function pushElement() public{
        b1.push('d');
    }
    function getElement(uint i) public view returns(bytes1){
        return b1[i];
    }
    function getLength() public view returns(uint){
        return b1.length;
    }
}

// Loops
// While Loops
contract While{
   uint[3] public arr;
   uint public count;

   function loop() public{
      while(count<arr.length){
         arr[count] = count;
         count++;
      }
   }
}

// For Loops
contract For{
   uint[3] public arr;
   uint public count;
   function loop() public{
      while(count<arr.length){
         arr[count] = count;
         count++;
      }
   }
}

// Do-While Loops
contract doWhile{
   uint[3] public arr;
   uint public count;
   function loop() public{
      do{
         arr[count] = count;
         count++;
      }while(count<arr.length);
   }
}

// If Else
contract ifElse{
   function check(int a) public pure returns(string memory){
      string memory value;
      if(a>0){
         value="greater than zero";
      }
      else if(a==0){
         value="equal to zero";
      }
      else{
         value="less than zero";
      }
      return value;
   }
}

// Boolean
contract Bool{
   bool public value=true;
   function check (uint a) public returns(bool){
      if(a>100){
         value=true;
         return value;
      }
      else{
         value=false;
         return value;
      }
   }
}

// Structure
struct Student{
   uint roll;
   string name;
}

contract Demo{
   Student public s1;
   constructor(uint _roll,string memory _name){
      s1.roll = _roll;
      s1.name = _name;
   }
     function change (uint _roll,string memory _name) public{
      Student memory new_student = Student({
         roll:_roll,
         name:_name
      });

      s1 = new_student;
   }
}

// Enum
contract Enum{
   enum user{allowed,not_allowed,wait}
   user public u1 = user.allowed;
   uint public lottery = 10000;
   function owner() public{
      if(u1==user.allowed){
         lottery = 0;
      }
   }
   function changeOwner() public{
      u1 = user.not_allowed;
   }
}


// Mapping
contract Mapping{
   mapping(uint=>string) public roll_no;
   function setter(uint keys,string memory value) public{
      roll_no[keys] = value;
   }
}

// Mapping with Struct
contract structMap{
   struct Student{
      string name;
      uint class;
   }
   mapping(uint=>Student) public data;
   function setter(uint _roll,string memory _name,uint _class) public{
      data[_roll]= Student(_name,_class);
   }
}

// Storage Vs Memory
contract memstor{
   string[] public student=['Ravi','Ram','Aman'];
   function mem() public view{
      string[] memory s1=student;
      s1[0]='Akash';
   }
   function sto() public{
      string[] storage s1=student;
      s1[0]='Akash';
   }
}

// Global Variable
contract blockDetails{
   function getter() public view returns(uint block_no,uint timestamp, address msgSender){
      return(block.number,block.timestamp,msgSender);
   }
}

// Balance Contract
contract pay{
   address payable user=payable(0xAb8483F64d9C6d1EcF9b849Ae677dD3315835cb2);
   function payEther() public payable{ 
   }
   function getBalanace() public view returns (uint){
      return address(this).balance;
   }
   function sendEtherAccount() public{
      user.transfer(1 ether);
   }
}
