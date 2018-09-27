# Maintainer: Yigit Dallilar <yigit.dallilar@gmail.com>

pkgname=spotiman
pkgver=0.1.0
pkgrel=1
pkgdesc="High level wrapper around spotipy"
arch=('x86_64')
url="https://github.com/pssncp142/spotiman"
license=('GPL3')
depends=('python-spotipy')
provides=('spotiman')
source=('spotiman::git+http://github.com/pssncp142/spotiman/')
source=("pyakm-$pkgver-$pkgrel.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=("d8ab26f0ea8fffc2eb96b362dae514915193662719307fd45a0a7609efa03e47")

prepare(){
	cd "$srcdir/spotiman-$pkgver"
}

package(){
	cd "$srcdir/spotiman-$pkgver"
	python setup.py install --root="$pkgdir/" --optimize=1
}

