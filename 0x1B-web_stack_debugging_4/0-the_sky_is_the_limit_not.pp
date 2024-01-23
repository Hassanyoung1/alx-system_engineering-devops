# Modifying Nginx request limits

exec { 'replace':
  provider => shell,
  command  => 'sed -i "s/15/10000/g" /etc/default/nginx && service nginx restart',
}

#exec { 'Restart Nginx':
 # provider => shell,
  #command  => 'service nginx restart',
#}
