from __future__ import annotations

from app.db.database import get_connection

COURSES = [
    {
        'slug': 'git-fundamentals',
        'title': 'Git Fundamentals',
        'description': 'Learn branches, commits, merges, and safe collaboration patterns.',
        'category': 'Version Control',
        'level': 'Beginner',
        'icon': 'GitBranch',
        'duration_minutes': 42,
        'order_index': 1,
    },
    {
        'slug': 'docker-essentials',
        'title': 'Docker Essentials',
        'description': 'Build, run, tag, and inspect containers with confidence.',
        'category': 'Containers',
        'level': 'Beginner',
        'icon': 'Package',
        'duration_minutes': 54,
        'order_index': 2,
    },
    {
        'slug': 'kubernetes-core',
        'title': 'Kubernetes Core',
        'description': 'Understand pods, deployments, services, and cluster workflows.',
        'category': 'Orchestration',
        'level': 'Intermediate',
        'icon': 'Layers',
        'duration_minutes': 68,
        'order_index': 3,
    },
    {
        'slug': 'terraform-infrastructure',
        'title': 'Terraform Infrastructure',
        'description': 'Provision cloud infrastructure with reusable IaC patterns.',
        'category': 'IaC',
        'level': 'Intermediate',
        'icon': 'Boxes',
        'duration_minutes': 61,
        'order_index': 4,
    },
]

LESSONS = [
    # Git
    {
        'course_slug': 'git-fundamentals',
        'slug': 'git-commit-flow',
        'title': 'Commit flow and branch safety',
        'description': 'Why small commits and clean branches make reviews easier.',
        'content': 'Use branches for isolated work, commit in small logical chunks, and keep history readable.',
        'code_example': 'git switch -c feature/branch-safety\ngit status\ngit add .\ngit commit -m "docs: improve branch safety"',
        'lesson_type': 'lesson',
        'minutes': 14,
        'order_index': 1,
    },
    {
        'course_slug': 'git-fundamentals',
        'slug': 'git-merge-vs-rebase',
        'title': 'Merge vs rebase',
        'description': 'Learn when to preserve history and when to linearize it.',
        'content': 'Merge keeps history visible; rebase rewrites local commits for a cleaner timeline.',
        'code_example': 'git fetch origin\ngit rebase origin/main\ngit push --force-with-lease',
        'lesson_type': 'lesson',
        'minutes': 13,
        'order_index': 2,
    },
    # Docker
    {
        'course_slug': 'docker-essentials',
        'slug': 'docker-images-layers',
        'title': 'Images, layers, and caching',
        'description': 'Understand how Docker builds repeatable images efficiently.',
        'content': 'Docker layers cache steps. Put changing files later in the Dockerfile to preserve cache hits.',
        'code_example': 'FROM node:20-alpine\nWORKDIR /app\nCOPY package*.json ./\nRUN npm ci\nCOPY . .',
        'lesson_type': 'lesson',
        'minutes': 18,
        'order_index': 1,
    },
    {
        'course_slug': 'docker-essentials',
        'slug': 'docker-container-lifecycle',
        'title': 'Container lifecycle and inspection',
        'description': 'Run, inspect, stop, and clean containers safely.',
        'content': 'Containers are ephemeral runtime instances created from images.',
        'code_example': 'docker run -d -p 3000:3000 --name web app\ndocker ps\ndocker logs web\ndocker rm -f web',
        'lesson_type': 'lesson',
        'minutes': 16,
        'order_index': 2,
    },
    # Kubernetes
    {
        'course_slug': 'kubernetes-core',
        'slug': 'k8s-pods-deployments',
        'title': 'Pods and deployments',
        'description': 'The basic deployment unit and the controller that keeps it stable.',
        'content': 'Pods are the smallest deployable unit. Deployments maintain desired replicas and rollout strategy.',
        'code_example': 'kubectl get pods -n platform\nkubectl rollout status deployment/api -n platform',
        'lesson_type': 'lesson',
        'minutes': 20,
        'order_index': 1,
    },
    {
        'course_slug': 'kubernetes-core',
        'slug': 'k8s-services-routing',
        'title': 'Services and routing',
        'description': 'Expose workloads safely inside and outside the cluster.',
        'content': 'Services give stable networking across ephemeral pods.',
        'code_example': 'kubectl expose deployment api --port=80 --target-port=8080\nkubectl get svc',
        'lesson_type': 'lesson',
        'minutes': 18,
        'order_index': 2,
    },
    # Terraform
    {
        'course_slug': 'terraform-infrastructure',
        'slug': 'terraform-state-plan-apply',
        'title': 'State, plan, and apply',
        'description': 'Use Terraform workflow steps to predict infrastructure changes.',
        'content': 'State tracks real resources. Plan previews changes. Apply makes them real.',
        'code_example': 'terraform init\nterraform plan\nterraform apply',
        'lesson_type': 'lesson',
        'minutes': 17,
        'order_index': 1,
    },
    {
        'course_slug': 'terraform-infrastructure',
        'slug': 'terraform-modules',
        'title': 'Modules for reuse',
        'description': 'Structure infrastructure as reusable building blocks.',
        'content': 'Modules help standardize infrastructure and reduce duplication.',
        'code_example': 'module "vpc" {\n  source = "./modules/vpc"\n}',
        'lesson_type': 'lesson',
        'minutes': 15,
        'order_index': 2,
    },
]

INITIAL_PROGRESS = [
    {'user_id': 1, 'course_slug': 'git-fundamentals', 'lesson_slug': 'git-commit-flow', 'is_completed': 1, 'percent': 100},
    {'user_id': 1, 'course_slug': 'docker-essentials', 'lesson_slug': 'docker-images-layers', 'is_completed': 1, 'percent': 100},
]


def seed_database() -> None:
    with get_connection() as connection:
        course_count = connection.execute('SELECT COUNT(*) AS total FROM courses').fetchone()['total']
        if course_count:
            return

        for course in COURSES:
            connection.execute(
                '''
                INSERT INTO courses (slug, title, description, category, level, icon, duration_minutes, order_index)
                VALUES (:slug, :title, :description, :category, :level, :icon, :duration_minutes, :order_index)
                ''',
                course,
            )

        course_ids = {
            row['slug']: row['id']
            for row in connection.execute('SELECT id, slug FROM courses').fetchall()
        }

        for lesson in LESSONS:
            connection.execute(
                '''
                INSERT INTO lessons (course_id, slug, title, description, content, code_example, lesson_type, minutes, order_index)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''',
                (
                    course_ids[lesson['course_slug']],
                    lesson['slug'],
                    lesson['title'],
                    lesson['description'],
                    lesson['content'],
                    lesson['code_example'],
                    lesson['lesson_type'],
                    lesson['minutes'],
                    lesson['order_index'],
                ),
            )

        lesson_lookup = {
            row['slug']: {'id': row['id'], 'course_id': row['course_id']}
            for row in connection.execute('SELECT id, course_id, slug FROM lessons').fetchall()
        }

        for progress in INITIAL_PROGRESS:
            lesson_meta = lesson_lookup[progress['lesson_slug']]
            connection.execute(
                '''
                INSERT INTO progress (user_id, course_id, lesson_id, is_completed, percent, attempts_count, completed_at, last_activity_at)
                VALUES (?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
                ''',
                (
                    progress['user_id'],
                    lesson_meta['course_id'],
                    lesson_meta['id'],
                    progress['is_completed'],
                    progress['percent'],
                    1,
                ),
            )
