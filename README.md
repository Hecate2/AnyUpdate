Not willing to deploy a new smart contract on Neo at a cost of 10 GAS? Use https://github.com/Hecate2/AnyUpdate that updates my contract to be yours, and invoke your own function! The storage written by you will be preserved by my contract!

The leading actor in this repo is `AnyUpdate.py`. Try it now at `0x68740b907e4fcb265c5ad339c38251b6f843577a` on the testnet!

This contract is expected to be a free public service, as well as an amazing showcase of smart contract self-updating. You may store anything in the contract (but the values might be overwritten by others). **Please do not overwrite the keys `original_nef_file` and `original_manifest` in the storage.**

Also `AnyUpdateSafe.py` is provided on the testnet at `0xb0b0d4bad5a8c17967ee30d997f0f1759c742402`. You can write on any key safely with this contract, though overwriting the keys `original_nef_file` and `original_manifest` is noneffective. `AnyUpdateSafe` costs more GAS than `AnyUpdate`.

Then `AnyUpdateShort.py` on testnet at `0x7cfe35715b3b2b9f3bc696f7483077434158d601` (with `findStorage` method supported!) gives a flexible way to give arguments to your methods. Note that a shorter contract does not always save your fee. Usually the fee is minimized when the length of my contract is close to that of yours.  We also have `AnyUpdateShortSafe.py` on testnet at `0x5c1068339fae89eb1a743909d0213e1d99dc5dc9`.

Finally there is an experimental project `AnyUpdateRenter.py` (`0x9cf19e43333a0b4513bd61e2316b40ecb9454a9b` on testnet) which allows you to rent contracts defined by `AnyUpdateSafeForRent.py` (instance 1 on testnet `0xb82bb0da46129f219d657cb6d7fbb22415efc502` that does not `findStorage`, instance 2 on testnet `0x6d13f393c90fa7182974a2b4d212e82bd0ccaf24` that supports `findStorage`, instance 3 on testnet `0xc2319a0e9c469598ba8c9425b56bcc39315c4c3e` that supports `findStorage` and `updateAndCallAnother`).

The test `tests/update_test.py`  using `Neo3vm` will not succeed because `_deploy` is an invalid method name. So just try an RPC test!

The test suite in this repository will not be maintained in the future, because it is a duplicate of that in https://github.com/Hecate2/neo-ruler/ . 

#### Usage

Please refer to [the RPC test for `AnyUpdate`](tests/update_rpc_test.py) and [the RPC test for `AnyUpdateSafe`](tests\safe_update_rpc_test.py). Update my contract to be yours, and invoke a function of your method in the same transaction. 

#### GAS cost

Calling `helloNeo` in my `AnyContract` costs a system fee of 0.53230593 GAS on testnet.

Calling `helloNeo` in my `AnyContractSafe` costs a system fee of 0.72147381 GAS on testnet.

#### Development

The contract is built with the following steps (Python 3.8 recommended):

1. In `AnyUpdate.py`, delete the `_deploy` method temporarily. Write anything in `AnyUpdate.py` and compile the contract with the command `neo3-boa AnyUpdate.py`. 
2. Record the raw `AnyUpdate.nef` file and `AnyUpdate.manifest.json`. You may refer to `engine.raw_nef` printed in `AnyUpdate/tests/update_test.py`. It is recommended to compress the json to save your GAS for deployment. 
3. Recover the `_deploy` method in `AnyUpdate.py`, filling the value of `original_nef_file` with the raw nef file, and `original_manifest` with the raw manifest json. 
4. Compile with `neo3-boa AnyUpdate.py` again and deploy the new `AnyUpdate.nef`!

#### Why do I use `get` and `put` but do not write fixed bytes of nef and json?

If I did write fixed nef and json, then I have to place the content of the whole program in a part of the program itself. This is impossible. 

#### Save more GAS...

For example, if your contract's methods need only 0 or 1 or 4 arguments (which is the case of basic NEP-17 contracts), you can deploy your own `AnyUpdate014.nef` deleting the methods for 2,3,5,6,7 arguments. Tell us the scripthash of your simplified contract if you would like to!

Additionally, if the length (in bytes) of your contract is approximately the same as mine, your GAS is saved according to [docs about GAS fees](https://docs.neo.org/docs/en-us/reference/fees.html#storage-fee).

**And certainly it costs NO GAS AT ALL if you do not relay your transaction.** Use `invokefunction(..., relay=False)` to cancel relaying with my test suite. 

