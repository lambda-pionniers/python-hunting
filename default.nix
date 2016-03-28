#
# Creation d'un environnement d'execution avec nix.
#
# Usage: nix-shell .
#
with import <nixpkgs> {};
with pkgs.python27Packages;

buildPythonPackage {
  name = "ninja";
  buildInputs = [
    stdenv
    python27Full
    pygame
  ];
}
