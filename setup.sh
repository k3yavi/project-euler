#new computer setup, bash script,
#NOTE: saving read only vim ```w !sudo tee % >/dev/null```

#Automatic log in
#generate ssh at local machine; you can leave passphrase blank
ssh-keygen -t rsa

#create .ssh folder in remote machine
ssh user@remote-ip mkdir -p .ssh

#paste rsa to remote
cat .ssh/id_rsa.pub | ssh user@remote-ip 'cat >> .ssh/authorized_keys'

#edit /etc/hosts to map name to ip
'remote-ip <name>' >> /etc/hosts

#login in to remote machine
ssh user@name

#install linubrew; Doesn't need admin
ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install)"

#set path
PATH="$HOME/.linuxbrew/bin:$PATH"

#install zsh
brew install zsh

#create .zshrc
mkdir -p ~/.zshrc

#add path to environment variable
echo 'export PATH="$HOME/.linuxbrew/bin:$PATH"' >>~/.profile

#set default shell as zsh
echo 'export SHELL=$(which zsh)
exec $(which zsh) -l' >> ~/.profile

