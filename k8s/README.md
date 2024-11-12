```sudo snap install kubectl --classic``` - установка kubectl

```export KUBECONFIG=путь_до_yaml_конфига``` (students.yaml)

```kubectl create ns название_неймспейса``` - создание неймспейса

```kubectl get ns``` - получить список неймспейсов

```kubectl apply -f deploy.yaml```

```kubectl delete -f deploy.yaml```

```kubectl get pod -n loykonen-matveev```

```kubectl exec -it -n loykonen-matveev mysql-0 -- /bin/bash```

```mysql -p```