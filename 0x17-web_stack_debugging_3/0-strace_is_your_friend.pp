# This Puppet manifest fixes wp-settings.php to resolve Internal Server Error

# Use sed to replace the incorrect line in wp-settings.php
exec { 'fix-wordpress':
  command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
  onlyif  => 'grep -q "class-wp-locale.phpp" /var/www/html/wp-settings.php',
  notify  => Service['apache2'],
}

# Ensure Apache is running and enabled
service { 'apache2':
  subscribe => Exec['fix-wordpress'],
}