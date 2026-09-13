import React from 'react';
import { theme } from '../theme';

interface DecisionBadgeProps {
  decision: 'allow' | 'challenge' | 'pause' | string;
  size?: 'sm' | 'md' | 'lg';
}

export const DecisionBadge: React.FC<DecisionBadgeProps> = ({ decision, size = 'md' }) => {
  const d = decision.toLowerCase();
  let bg = theme.colors.allowBg;
  let border = theme.colors.allowBorder;
  let color = theme.colors.allow;
  let label = 'ALLOW';

  if (d === 'challenge') {
    bg = theme.colors.challengeBg;
    border = theme.colors.challengeBorder;
    color = theme.colors.challenge;
    label = 'CHALLENGE';
  } else if (d === 'pause') {
    bg = theme.colors.pauseBg;
    border = theme.colors.pauseBorder;
    color = theme.colors.pause;
    label = 'PAUSE';
  }

  const padding = size === 'sm' ? '4px 10px' : size === 'lg' ? '10px 24px' : '6px 14px';
  const fontSize = size === 'sm' ? '12px' : size === 'lg' ? '22px' : '15px';

  return (
    <span
      style={{
        display: 'inline-flex',
        alignItems: 'center',
        justifyContent: 'center',
        padding,
        backgroundColor: bg,
        border: `1.5px solid ${border}`,
        borderRadius: '6px',
        color,
        fontWeight: 700,
        fontFamily: theme.fonts.mono,
        fontSize,
        letterSpacing: '1px',
        textTransform: 'uppercase',
      }}
    >
      {label}
    </span>
  );
};
