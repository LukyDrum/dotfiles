#!/bin/bash

CONFIG_DIR=~/.config

echo "This will replace your current configurations inside $CONFIG_DIR."
echo "Are you sure you want to continue?"
select yn in "Yes" "No";
do
    case $yn in
        Yes ) echo "Starting roll-out!"; break;;
        No ) exit;;
    esac
done

# Roll out NeoVim config
rm -rf $CONFIG_DIR/nvim
cp -r nvim $CONFIG_DIR/nvim

echo "Roll-out done!"
