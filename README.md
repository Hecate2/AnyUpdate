Not willing to deploy a new smart contract on Neo at a cost of 10 GAS? Use https://github.com/Hecate2/AnyUpdate that updates my contract to be yours, and invoke your own function!  

The leading actor in this repo is `AnyUpdate.py`. Try it now at `0x92be0911dd55671a69362c807dc2c452404834c0` on the testnet!

This contract is expected to be a free public service, as well as an amazing showcase of smart contract self-updating. You may store anything in the contract (but the values might be overwritten by others). **Please do not overwrite the keys `original_nef_file` and `original_manifest` in the storage.**

The test `tests/update_test.py`  using `Neo3vm` will not succeed because `_deploy` is an invalid method name. Try an RPC test on the testnet or your private net!

The test suite in this repository will not be maintained in the future, because it is a duplicate of that in https://github.com/Hecate2/neo-ruler/ . 

#### Usage

Please refer to [the RPC test](tests/update_rpc_test.py). Update my contract to be yours, and invoke a function of your method in the same transaction. Calling `helloNeo` in my AnyContract costs a system fee of 0.54300593 GAS on testnet.

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