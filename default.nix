#
# Creation d'un environnement d'execution avec nix.
#
# Usage: nix-shell .
#
with import <nixpkgs> {};
with pkgs.python27Packages;

buildPythonPackage {
  name = "Python hunter";
  buildInputs = [
    stdenv
    python27Full
    pygame
  ];
}
