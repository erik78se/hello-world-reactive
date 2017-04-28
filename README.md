This tutorial covers basics of developing a juju charm with a "base layer".

A "base layer" (as I interpret it) is a charm that holds some common functionality, perhaps package installations you normally use or deploys code common to all your applications in charms you develop.

The layer we will develop here will do very little.

Make sure to complete the "hello-world" tutorial before starting this one.

# Create the "layers" working space

    mkdir -p ~/git/juju/layers
