// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * TinyCoin ERC20
 * Week 15 - Proyek Kelompok
 * Implementasi token ERC20 sederhana
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract TinyCoin is ERC20 {

    // Constructor dijalankan sekali saat kontrak di-deploy
    constructor(uint256 initialSupply) ERC20("TinyCoin", "TNC") {
        // Mint token awal ke alamat deployer
        _mint(msg.sender, initialSupply);
    }
}
