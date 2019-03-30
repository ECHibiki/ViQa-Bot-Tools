<?php
// replace thse on your config and create a new user for your bot
// store the login cookie
$config['mod']['groups'] = array(
  5   => 'Bot',
  10	=> 'Janitor',
  20	=> 'Mod',
  30	=> 'Admin',
  // 98	=> 'God',
  99	=> 'Disabled'
);

$config['mod']['capcode'] = array(
  BOT   => array('Bot'),
  JANITOR		=> array('Janitor'),
  MOD		=> array('Mod'),
  ADMIN		=> true
);

$config['mod']['rebuild'] = BOT;
 ?>
