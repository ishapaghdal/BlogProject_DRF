import { Routes } from '@angular/router';
import { TasksComponent } from './tasks/tasks.component';
import { NoTaskComponent } from './tasks/no-task/no-task.component';
import { UserTasksComponent } from './users/user-tasks/user-tasks.component';
import { NewTaskComponent } from './tasks/new-task/new-task.component';
import { NotFoundError } from 'rxjs';
import {routes as userRoutes} from './users/users.routes'

export const routes: Routes = [
  {
    path: '',
    component: NoTaskComponent,
    // redirectTo : '/users/u1',
    // pathMatch:'full'
  },
  {
    path: 'users/:userId',
    component: UserTasksComponent,
    children: userRoutes,
    data: {
      message : 'Hii Isha'
    },
    resolve : {
      
    }
  },
  {
    path: '**',
    component: NoTaskComponent,
  },
];
