# file should contain Puppet code
# You can use whatever Puppet resource type you want for you fix

exec { 'fix_phpp':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin/', '/usr/loca/bin/'],
}
