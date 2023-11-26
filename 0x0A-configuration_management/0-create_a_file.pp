file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => '_www',
  group   => '_www',
  content => 'I love Puppet',
}

