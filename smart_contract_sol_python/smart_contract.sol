// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Voting {
    
    // Estructura que define a un candidato
    struct Candidate {
        uint id;
        string name;
        uint voteCount;
    }
    
    // Mapeo para almacenar los candidatos
    mapping(uint => Candidate) public candidates;
    
    // Mapeo para rastrear si una dirección ya ha votado
    mapping(address => bool) public hasVoted;

    // Contador de candidatos
    uint public candidatesCount;

    // Evento para registrar que se emitió un voto
    event Voted(address indexed voter, uint indexed candidateId);

    // Constructor para agregar candidatos al contrato
    constructor() {
        addCandidate("Candidate 1");
        addCandidate("Candidate 2");
    }
    
    // Función para agregar un candidato
    function addCandidate(string memory _name) private {
        candidatesCount++;
        candidates[candidatesCount] = Candidate(candidatesCount, _name, 0);
    }

    // Función para votar por un candidato
    function vote(uint _candidateId) public {
        // Verificar que el votante no haya votado antes
        require(!hasVoted[msg.sender], "You have already voted.");

        // Verificar que el candidato exista
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID.");

        // Registrar que el votante ha votado
        hasVoted[msg.sender] = true;

        // Incrementar el conteo de votos del candidato
        candidates[_candidateId].voteCount++;

        // Emitir un evento que se emitió un voto
        emit Voted(msg.sender, _candidateId);
    }

    // Función para obtener el número de votos de un candidato
    function getVoteCount(uint _candidateId) public view returns (uint) {
        require(_candidateId > 0 && _candidateId <= candidatesCount, "Invalid candidate ID.");
        return candidates[_candidateId].voteCount;
    }
}
