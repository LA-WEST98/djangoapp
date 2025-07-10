Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.synced_folder "C:/Users/user/Desktop/django_project/djangoapp/django-devops", "/home/vagrant/devops-django/django-devops"
  config.vm.hostname = "devops-django"
  config.vm.network "private_network", ip: "192.168.56.12"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end

  config.vm.provision "shell", path: "provision.sh"
end
