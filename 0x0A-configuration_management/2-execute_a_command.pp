# Kills a process named killmenow

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  onlyif      => 'pgrep -f killmenow',
  refreshonly => true,
}
