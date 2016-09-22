#new computer setup, bash script, Does not requires admin
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

#install oh my zsh
#download shell scriopt for oh-myzsh
wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh

#edit and delete line 30 from downloaded file install.sh i.e. exit from line 30
#execute install.sh
chmod +x install.sh && ./install.sh
rm install.sh

#change theme rubyrushell to bira in ~/.zshrc line 10

#install miniconda
#link here is for python 3
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
chmod +x Miniconda3-latest-Linux-x86_64.sh && ./Miniconda3-latest-Linux-x86_64.sh
rm Miniconda3-latest-Linux-x86_64.sh

#add miniconda path to zshrc
echo 'export PATH="PATH=$HOME/miniconda3/bin:$PATH"' >>~/.zshrc

#install spf-13
sh <(curl https://j.mp/spf13-vim3 -L)

#install supplementary tools
brew install tmux
