import {
  Component,
  computed,
  DestroyRef,
  inject,
  input,
  OnInit,
} from '@angular/core';
import { UsersService } from '../users.service';
import { ActivatedRoute, ActivatedRouteSnapshot, ResolveFn, RouterLink, RouterOutlet, RouterStateSnapshot } from '@angular/router';
import { __param } from 'tslib';

@Component({
  selector: 'app-user-tasks',
  standalone: true,
  imports: [RouterOutlet,RouterLink],
  templateUrl: './user-tasks.component.html',
  styleUrl: './user-tasks.component.css',
})
export class UserTasksComponent implements OnInit {
  // userId = input.required<string>();
  userName = '';
  private userService = inject(UsersService);
  private activatedRoute = inject(ActivatedRoute);
  private destroyRef = inject(DestroyRef);
  message = input.required<string>();
  // userName = computed(() => this.userS ervice.users.find(u => u.id === this.userId())?.name)

  ngOnInit(): void {
    console.log(this.message);
    
    console.log(this.activatedRoute);
    
    const subscription = this.activatedRoute.paramMap.subscribe({
      next: (paramMap) =>
        (this.userName =
          this.userService.users.find((u) => u.id === paramMap.get('userId'))
            ?.name || ''),
    });

  this.destroyRef.onDestroy(() => subscription.unsubscribe());

  }

}

// export const resolveUserName: ResolveFn = (activatedRoute: ActivatedRouteSnapshot , routerState : RouterStateSnapshot)=>{

//   const UserService = inject(UsersService);
//   return 

// };
