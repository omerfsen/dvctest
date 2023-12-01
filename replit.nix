{ pkgs }: {
  deps = [
    pkgs.openssh
    pkgs.dvc
    pkgs.azure-cli
    pkgs.docker-compose
    pkgs.docker
  ];
}