# Install Nginx if not already installed
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

# Create necessary directories
file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static/releases':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static/shared':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

file { '/data/web_static/releases/test':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# Create a fake HTML file for testing
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  content => "<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n",
}

# Create a symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  force   => true,
}

# Update Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "server {\n
  listen 80;\n
  server_name _;\n
  location /hbnb_static {\n
  alias /data/web_static/current;\n}\n}\n",
  notify  => Service['nginx'],
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
}
