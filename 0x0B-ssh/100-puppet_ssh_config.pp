#!/usr/bin/env bash
# using Puppet to make changes to our configuration
# Requirements: use the private key ~/.ssh/school, using a password

file { '/etc/ssh/ssh_config':
  ensure  => present,
content => "
    # SSH client configuration
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
