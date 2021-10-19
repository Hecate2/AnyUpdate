Not willing to deploy a new smart contract on Neo at a cost of 10 GAS? Use https://github.com/Hecate2/AnyUpdate that updates my contract to be yours, and invoke your own function!  

This is expected to be a free public service, as well as an amazing showcase of smart contract self-updating. Please do not overwrite the keys `original_nef_file` and `original_manifest` in the storage. 

The test `tests/update_test.py`  using `Neo3vm` will not succeed because `_deploy` is an invalid method name. Try an RPC test on the testnet or your private net!

