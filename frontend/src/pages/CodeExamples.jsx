import { CodeBlock } from '@/shared/code/CodeBlock.jsx'
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from '@/shared/ui/Card.jsx'

const K8S = `apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
  namespace: platform
spec:
  replicas: 2
  selector:
    matchLabels:
      app: api
  template:
    metadata:
      labels:
        app: api
    spec:
      containers:
        - name: api
          image: ghcr.io/acme/api:1.2.3
          ports:
            - containerPort: 8080
          readinessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 5
            periodSeconds: 5
`

const GHA = `name: CI

on:
  push:
    branches: [ main ]
  pull_request:

jobs:
  build-test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm test
      - run: npm run build
`

const DOCKER = `# Multi-stage build for a React app
FROM node:20-alpine AS build
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
`

export function CodeExamples() {
    return (
        <div className="space-y-6">
            <div>
                <div className="text-2xl font-semibold tracking-tight">Code examples</div>
                <p className="mt-1 text-sm text-muted">
                    Reference snippets with readable syntax styling for DevOps workflows.
                </p>
            </div>

            <div className="grid gap-6 lg:grid-cols-2">
                <Card>
                    <CardHeader>
                        <CardTitle>Kubernetes deployment</CardTitle>
                        <CardDescription>Deployment + readiness probe</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <CodeBlock title="deployment.yaml" language="yaml" code={K8S} />
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>GitHub Actions CI</CardTitle>
                        <CardDescription>Build + test + artifact pipeline</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <CodeBlock title=".github/workflows/ci.yml" language="yaml" code={GHA} />
                    </CardContent>
                </Card>

                <Card className="lg:col-span-2">
                    <CardHeader>
                        <CardTitle>Docker multi-stage build</CardTitle>
                        <CardDescription>Small images, predictable builds</CardDescription>
                    </CardHeader>
                    <CardContent>
                        <CodeBlock title="Dockerfile" language="bash" code={DOCKER} />
                    </CardContent>
                </Card>
            </div>
        </div>
    )
}
