# Dotfiles
First install pacaur. Do this by running the following commands AS NORMAL USER:
  sudo pacman -S expac yajl --noconfirm
  mkdir ~/tmp
  cd ~/tmp/
  gpg --recv-keys --keyserver hkp://pgp.mit.edu 1EB2638FF56C0C53
  curl -o PKGBUILD https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=cower
  makepkg -i PKGBUILD --noconfirm
  curl -o PKGBUILD https://aur.archlinux.org/cgit/aur.git/plain/PKGBUILD?h=pacaur
  makepkg -i PKGBUILD --noconfirm
  cd
  rm -r ~/tmp
Then, install packages from pkglist.txt, using 'pacaur -S - < pkglist.txt'
