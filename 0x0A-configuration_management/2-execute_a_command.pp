# Execute a command

exec { 'killmenow':
    command     => 'pkill killmenow',
    path        => ['/bin', '/usr/bin'],
    onlyif      => 'pgrep killnow',
    refreshonly => true,
}


