# Execute a command

exec { 'killmenow':
    command     => 'pkill -f killmenow',
    path        => ['/bin:/usr/bin'],
    onlyif      => 'pgrep -f killnow',
    refreshonly => true,
    logoutput   => true,
}


