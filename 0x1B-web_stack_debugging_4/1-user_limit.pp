# Modifying open files limits
exec { 'Fix File limit':
  provider    => 'shell',
  command     => 'sed -i "s/5/10000/g; s/4/10000/g" /etc/security/limits.conf',
}
