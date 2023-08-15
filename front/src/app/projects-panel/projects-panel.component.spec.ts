import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProjectsPanelComponent } from './projects-panel.component';

describe('ProjectsPanelComponent', () => {
  let component: ProjectsPanelComponent;
  let fixture: ComponentFixture<ProjectsPanelComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [ProjectsPanelComponent]
    });
    fixture = TestBed.createComponent(ProjectsPanelComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
