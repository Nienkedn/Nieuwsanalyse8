# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "generic/ubuntu1804"

  # Share an additional folder to the guest VM. The first argument is
  # the path on the host to the actual folder. The second argument is
  # the path on the guest to mount the folder. And the optional third
  # argument is a set of non-required options.
  config.vm.synced_folder ".", "/code"

  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.

  config.vm.provision "shell", privileged: "false", inline: <<-SHELL
  apt-get install python3-pip -y
  echo " "
  echo "======================================================================="
  echo "Writing aliases to profile."
  echo ""
  echo "NOTE: Ignore the possible error about inappropriate ioctl devices."
  echo ""
  echo "The aliases were configured successfully."
  echo ""
  echo "Check it by typing:"
  echo ""
  echo "    python --version"
  echo ""
  echo "in the console. It should return:"
  echo ""
  echo "    Python 3.6.X"
  echo ""
  echo "======================================================================="
  echo ""
  echo "alias python=\"python3\"" >> /home/vagrant/.profile
  echo "alias pip=pip3" >> /home/vagrant/.profile
  cd /code
  pip3 install -r requirements.txt
  . ~/.profile
  SHELL
end
