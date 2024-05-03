mayapy -m pyeal build
$dirname = Split-Path -Path $PWD -Leaf
7z -tzip a "./build/${dirname}.zip" ./build/out/*